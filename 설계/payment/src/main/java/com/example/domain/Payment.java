package com.example.domain;

import lombok.Getter;

@Getter
public class Payment {
    private final Pg pg;
    private final PaymentType paymentType;

    public Payment(Pg pg, PaymentType paymentType) {
        this.pg = pg;
        this.paymentType = paymentType;
    }
}
