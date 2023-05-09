package com.example.service;

import com.example.domain.Payment;
import com.example.domain.PaymentType;
import com.example.domain.Pg;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class PaymentServiceTest {

    @Autowired
    private PaymentService paymentService;

    @Test
    void test() {
        Payment cardOne = new Payment(Pg.ONE, PaymentType.CARD);
        Payment cardTwo = new Payment(Pg.TWO, PaymentType.CARD);
        Payment cardThree = new Payment(Pg.THREE, PaymentType.CARD);
        Payment bank = new Payment(Pg.BANK, PaymentType.BANK);

        paymentService.pay(cardOne);
        paymentService.pay(cardTwo);
        paymentService.pay(cardThree);
        paymentService.pay(bank);
    }
}
