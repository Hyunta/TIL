package money;

class Money implements Expression{
    protected int amount;
    protected String currency;

    public boolean equals(Object object) {
        Money money = (Money) object;
        return amount == money.amount
                && currency().equals(money.currency());
    }

    public Money reduce(String to) {
        return this;
    }

    Money times(int multiplier) {
        return new Money(amount * multiplier, currency);
    }

    Expression plus(Money addend) {
        return new Sum(this, addend);
    }

    static Money dollar(int amount) {
        return new Money(amount, "USD");
    }

    static Money franc(int amount) {
        return new Money(amount, "CHF");
    }


    String currency() {
        return currency;
    }

    public Money(int amount, String currency) {
        this.amount = amount;
        this.currency = currency;
    }


    public String toString() {
        return amount + " " + currency;
    }
}
