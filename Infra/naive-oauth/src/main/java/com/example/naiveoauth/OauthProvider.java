package com.example.naiveoauth;

import lombok.Builder;
import lombok.Getter;

@Getter
@Builder
public class OauthProvider {
    private final String clientId;
    private final String clientSecret;
    private final String redirectUri;
    private final String tokenUri;
    private final String userInfoUri;

    public OauthProvider(OauthProperties.User user, OauthProperties.Provider provider) {
        this(user.getClientId(), user.getClientSecret(), user.getRedirectUri(), provider.getTokenUri(),
                provider.getUserInfoUri());
    }

    public OauthProvider(String clientId, String clientSecret, String redirectUri, String tokenUri,
                         String userInfoUri) {
        this.clientId = clientId;
        this.clientSecret = clientSecret;
        this.redirectUri = redirectUri;
        this.tokenUri = tokenUri;
        this.userInfoUri = userInfoUri;
    }
}
