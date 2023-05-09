package com.example.service;

import com.example.payment.BankPaymentClient;
import com.example.dto.request.BankRequest;
import com.example.dto.response.BankResponse;
import com.example.payment.CardOnePaymentClient;
import com.example.dto.request.CardOneRequest;
import com.example.dto.response.CardOneResponse;
import com.example.payment.CardThreePaymentClient;
import com.example.dto.request.CardThreeRequest;
import com.example.dto.response.CardThreeResponse;
import com.example.payment.CardTwoPaymentClient;
import com.example.dto.request.CardTwoRequest;
import com.example.dto.response.CardTwoResponse;
import com.example.domain.Payment;
import com.example.domain.PaymentType;
import com.example.domain.Pg;
import org.springframework.stereotype.Service;

@Service
public class PaymentService {

    private final BankPaymentClient bankPaymentClient;
    private final CardOnePaymentClient cardOnePaymentClient;
    private final CardTwoPaymentClient cardTwoPaymentClient;
    private final CardThreePaymentClient cardThreePaymentClient;

    public PaymentService(BankPaymentClient bankPaymentClient, CardOnePaymentClient cardOnePaymentClient,
                          CardTwoPaymentClient cardTwoPaymentClient, CardThreePaymentClient cardThreePaymentClient) {
        this.bankPaymentClient = bankPaymentClient;
        this.cardOnePaymentClient = cardOnePaymentClient;
        this.cardTwoPaymentClient = cardTwoPaymentClient;
        this.cardThreePaymentClient = cardThreePaymentClient;
    }

    public void pay(Payment payment) {
        if (payment.getPaymentType().equals(PaymentType.CARD)) {
            if (payment.getPg().equals(Pg.ONE)) {
                requestCardOne(payment);
            }
            if (payment.getPg().equals(Pg.TWO)) {
                requestCardTwo(payment);
            }
            if (payment.getPg().equals(Pg.THREE)) {
                requestCardThree(payment);
            }
            throw new IllegalArgumentException();
        }

        if (payment.getPaymentType().equals(PaymentType.BANK)) {
            requestBank(payment);
        }
        throw new IllegalArgumentException();
    }

    private CardOneResponse requestCardOne(Payment payment) {
        CardOneRequest request = CardOneRequest.of(payment);
        CardOneResponse response = cardOnePaymentClient.pay(request);
        return response;
    }

    private CardTwoResponse requestCardTwo(Payment payment) {
        CardTwoRequest request = CardTwoRequest.of(payment);
        CardTwoResponse response = cardTwoPaymentClient.pay(request);
        return response;
    }

    private CardThreeResponse requestCardThree(Payment payment) {
        CardThreeRequest request = CardThreeRequest.of(payment);
        CardThreeResponse response = cardThreePaymentClient.pay(request);
        return response;
    }

    private BankResponse requestBank(Payment payment) {
        BankRequest request = BankRequest.of(payment);
        BankResponse response = bankPaymentClient.pay(request);
        return response;
    }
}
