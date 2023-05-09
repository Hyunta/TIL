package com.example.payment;

import com.example.dto.request.BankRequest;
import com.example.dto.response.BankResponse;
import org.springframework.stereotype.Component;

@Component
public class BankPaymentClient {

    public BankResponse pay(BankRequest request) {

        return new BankResponse();
    }
}
