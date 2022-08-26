package com.example.naiveoauth;

public class OauthService {

    private final InMemoryProviderRepository inMemoryProviderRepository;

    public OauthService(InMemoryProviderRepository inMemoryProviderRepository) {
        this.inMemoryProviderRepository = inMemoryProviderRepository;
    }

    public LoginResponse login(String providerName, String code) {
        OauthProvider provider = inMemoryProviderRepository.findByProviderName(providerName);
        return null;
    }
}
