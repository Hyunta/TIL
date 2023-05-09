package com.example.payment;

import com.example.dto.request.CardThreeRequest;
import com.example.dto.request.PaymentRequest;
import com.example.dto.response.CardThreeResponse;
import com.example.dto.response.PaymentResponse;
import org.springframework.stereotype.Component;

@Component
public class CardThreePaymentClient implements PaymentClient {

    public CardThreeResponse pay(PaymentRequest request) {
        //do something
        return new CardThreeResponse();
    }
}
