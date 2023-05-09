package com.example.payment;

import com.example.dto.request.CardThreeRequest;
import com.example.dto.response.CardThreeResponse;
import org.springframework.stereotype.Component;

@Component
public class CardThreePaymentClient {
    public CardThreeResponse pay(CardThreeRequest request) {
        //do something
        return new CardThreeResponse();
    }
}
