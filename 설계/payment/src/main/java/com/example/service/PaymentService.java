package com.example.service;

import com.example.domain.Payment;
import com.example.domain.Pg;
import com.example.dto.request.PaymentRequest;
import com.example.payment.PaymentClient;
import java.util.Arrays;
import org.springframework.stereotype.Service;

@Service
public class PaymentService {

    public void pay(Payment payment) {
        PaymentRequest paymentRequest = findPaymentRequest(payment);
        PaymentClient paymentClient = findPaymentClient(payment);

        paymentClient.pay(paymentRequest);
    }

    private static PaymentClient findPaymentClient(Payment payment) {
        return Arrays.stream(Pg.values())
                .filter(it -> it.equals(payment.getPg()))
                .findAny()
                .map(Pg::getClient)
                .orElseThrow(IllegalArgumentException::new);
    }

    private static PaymentRequest findPaymentRequest(Payment payment) {
        return Arrays.stream(Pg.values())
                .filter(it -> it.equals(payment.getPg()))
                .findAny()
                .map(Pg::getRequest)
                .orElseThrow(IllegalArgumentException::new);
    }
}
