package com.example.payment;

import org.springframework.stereotype.Component;

@Component
public class CardTwoPaymentClient {
    public CardTwoResponse pay(CardTwoRequest request) {
        //do simething
        return new CardTwoResponse();
    }
}
