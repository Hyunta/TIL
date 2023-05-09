package com.example.dto.request;

import com.example.domain.Payment;

public class CardThreeRequest implements PaymentRequest{

    public static CardThreeRequest of(Payment payment) {
        return new CardThreeRequest();
    }
}
