package com.example.domain;

import com.example.dto.request.BankRequest;
import com.example.dto.request.CardOneRequest;
import com.example.dto.request.CardThreeRequest;
import com.example.dto.request.CardTwoRequest;
import com.example.dto.request.PaymentRequest;
import com.example.payment.BankPaymentClient;
import com.example.payment.CardOnePaymentClient;
import com.example.payment.CardThreePaymentClient;
import com.example.payment.CardTwoPaymentClient;
import com.example.payment.PaymentClient;
import java.util.function.Supplier;

public enum Pg {
    ONE(CardOneRequest::new, CardOnePaymentClient::new),
    TWO(CardTwoRequest::new, CardTwoPaymentClient::new),
    THREE(CardThreeRequest::new, CardThreePaymentClient::new),
    BANK(BankRequest::new, BankPaymentClient::new),
    ;

    private final Supplier<PaymentRequest> requestSupplier;
    private final Supplier<PaymentClient> clientSupplier;

    Pg(Supplier<PaymentRequest> requestSupplier, Supplier<PaymentClient> clientSupplier) {
        this.requestSupplier = requestSupplier;
        this.clientSupplier = clientSupplier;
    }

    public PaymentRequest getRequest() {
        return this.requestSupplier.get();
    }

    public PaymentClient getClient() {
        return this.clientSupplier.get();
    }
}
