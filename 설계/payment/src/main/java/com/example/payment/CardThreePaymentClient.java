package com.example.payment;

import org.springframework.stereotype.Component;

@Component
public class CardThreePaymentClient {
    public CardThreeResponse pay(CardThreeRequest request) {
        //do something
        return new CardThreeResponse();
    }
}
