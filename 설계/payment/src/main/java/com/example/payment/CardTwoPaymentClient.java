package com.example.payment;

import com.example.dto.request.CardTwoRequest;
import com.example.dto.response.CardTwoResponse;
import org.springframework.stereotype.Component;

@Component
public class CardTwoPaymentClient {
    public CardTwoResponse pay(CardTwoRequest request) {
        //do simething
        return new CardTwoResponse();
    }
}
