package com.example.dto.request;

import com.example.domain.Payment;

public class CardThreeRequest {

    public static CardThreeRequest of(Payment payment) {
        return new CardThreeRequest();
    }
}
