package com.example.payment;

import com.example.dto.request.PaymentRequest;
import com.example.dto.response.CardTwoResponse;
import com.example.dto.response.PaymentResponse;
import org.springframework.stereotype.Component;

@Component
public class CardTwoPaymentClient implements PaymentClient {

    @Override
    public CardTwoResponse pay(PaymentRequest paymentRequest) {
        //do something
        return new CardTwoResponse();
    }
}
