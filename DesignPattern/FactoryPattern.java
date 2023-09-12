package DesignPattern;

// Factory Pattern
// 추상화 된 객체를 생성하는 패턴 (객체 생성을 캡슐화)
abstract class Coffee {
    public abstract int getPrice();

    @Override
    public String toString() {
        return "Hi, this coffee is: " + this.getPrice();
    }
}

class CoffeeFactory {
    // Factory Method
    public static Coffee getCoffee(String type, int price) {
        if ("Latte".equalsIgnoreCase(type)) {
            return new Latte(price);
        } else if ("Americano".equalsIgnoreCase(type)) {
            return new Americano(price);
        } else {
            return new DefaultCoffee();
            //throw new IllegalArgumentException("This type of coffee is not supported: " + type);
        } 
    }
}

// Default Coffee is not supported by the factory pattern
class DefaultCoffee extends Coffee {

    private int price;

    public DefaultCoffee(){
        this.price = -1;
    }
    
    @Override
    public int getPrice() {
        return this.price;
    }

}

class Latte extends Coffee {
    private int price;

    public Latte(int price){
        this.price = price;
    }

    @Override
    public int getPrice() {
        return   this.price;
    }
}

class Americano extends Coffee {
    private int price;

    public Americano(int price){
        this.price = price;
    }

    @Override
    public int getPrice() {
        return this.price;
    }
}

public class FactoryPattern {
    public static void main(String[] args) {
        Coffee latte = CoffeeFactory.getCoffee("Latte", 1000);
        Coffee americano = CoffeeFactory.getCoffee("Americano", 500);
        Coffee defaultCoffee = CoffeeFactory.getCoffee("Default", 500);

        System.out.println(latte);
        System.out.println(americano);
        System.out.println(defaultCoffee);
    }
}