package com.example.payment;

import com.example.dto.request.PaymentRequest;
import com.example.dto.response.CardOneResponse;
import org.springframework.stereotype.Component;

@Component
public class CardOnePaymentClient implements PaymentClient {

    public CardOneResponse pay(PaymentRequest request) {
        //do something
        return new CardOneResponse();
    }
}
