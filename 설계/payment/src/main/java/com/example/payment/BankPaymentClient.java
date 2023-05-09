package com.example.payment;

import com.example.dto.request.PaymentRequest;
import com.example.dto.response.BankResponse;
import org.springframework.stereotype.Component;

@Component
public class BankPaymentClient implements PaymentClient {

    public BankResponse pay(PaymentRequest request) {

        return new BankResponse();
    }
}
