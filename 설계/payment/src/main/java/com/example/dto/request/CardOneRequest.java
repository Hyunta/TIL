package com.example.dto.request;

import com.example.domain.Payment;

public class CardOneRequest {

    public static CardOneRequest of(Payment payment) {
        return new CardOneRequest();
    }
}
