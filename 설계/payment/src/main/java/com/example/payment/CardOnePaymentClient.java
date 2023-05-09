package com.example.payment;

import com.example.dto.request.CardOneRequest;
import com.example.dto.response.CardOneResponse;
import org.springframework.stereotype.Component;

@Component
public class CardOnePaymentClient {

    public CardOneResponse pay(CardOneRequest request) {
        //do something
        return new CardOneResponse();
    }
}
