package com.example.payment;

import com.example.dto.request.PaymentRequest;
import com.example.dto.response.PaymentResponse;

public interface PaymentClient {

    PaymentResponse pay(PaymentRequest paymentRequest);

}
