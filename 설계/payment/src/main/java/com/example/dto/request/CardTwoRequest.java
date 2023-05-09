package com.example.dto.request;

import com.example.domain.Payment;

public class CardTwoRequest {

    public static CardTwoRequest of(Payment payment) {
        return new CardTwoRequest();
    }
}
