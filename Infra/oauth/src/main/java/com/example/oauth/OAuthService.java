package com.example.oauth;

import java.util.Collections;
import java.util.Map;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.oauth2.client.userinfo.DefaultOAuth2UserService;
import org.springframework.security.oauth2.client.userinfo.OAuth2UserRequest;
import org.springframework.security.oauth2.client.userinfo.OAuth2UserService;
import org.springframework.security.oauth2.core.OAuth2AuthenticationException;
import org.springframework.security.oauth2.core.user.DefaultOAuth2User;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.stereotype.Service;

@Service
public class OAuthService implements OAuth2UserService<OAuth2UserRequest, OAuth2User> {

    private final Logger log = LoggerFactory.getLogger(OAuthService.class);
    private final MemberRepository memberRepository;

    public OAuthService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

    @Override
    public OAuth2User loadUser(OAuth2UserRequest userRequest) throws OAuth2AuthenticationException {
        DefaultOAuth2UserService delegate = new DefaultOAuth2UserService();
        OAuth2User oAuth2User = delegate.loadUser(userRequest);

        String registrationId = userRequest.getClientRegistration()
                .getRegistrationId();
        String userNameAttributeName = userRequest.getClientRegistration().getProviderDetails()
                .getUserInfoEndpoint().getUserNameAttributeName();
        Map<String, Object> attributes = oAuth2User.getAttributes();

        String email = (String) attributes.get("email");
        log.info(email);
        log.info(attributes.keySet().toString());
        UserProfile userProfile = OAuthAttributes.extract(registrationId, attributes);

        Member member = saveOrUpdate(userProfile);

        return new DefaultOAuth2User(
                Collections.singleton(new SimpleGrantedAuthority(member.getRoleKey())),
                attributes,
                userNameAttributeName
        );
    }

    private Member saveOrUpdate(UserProfile userProfile) {
        log.info(userProfile.getEmail());
        Member member = memberRepository.findByOauthId(userProfile.getOauthId())
                .map(it -> it.update(userProfile.getName(), userProfile.getEmail(), userProfile.getImageUrl()))
                .orElse(userProfile.toMember());
        return memberRepository.save(member);
    }
}
