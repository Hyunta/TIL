package com.example.payment;

import org.springframework.stereotype.Component;

@Component
public class BankPaymentClient {

    public BankResponse pay(BankRequest request) {

        return new BankResponse();
    }
}
