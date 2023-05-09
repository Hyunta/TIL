package com.example.dto.request;

import com.example.domain.Payment;

public class BankRequest implements PaymentRequest{
    public static BankRequest of(Payment payment) {
        return new BankRequest();
    }
}
