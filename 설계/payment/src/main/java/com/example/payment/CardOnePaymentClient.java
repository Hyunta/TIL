package com.example.payment;

import org.springframework.stereotype.Component;

@Component
public class CardOnePaymentClient {

    public CardOneResponse pay(CardOneRequest request) {
        //do something
        return new CardOneResponse();
    }
}
