package encapsulation;

public class Account {

	private double beløp;
	private double renter;
	
	Account(double start, double rente){
		if(start < 1 || rente < 1) {
			throw new IllegalArgumentException("Må ha positive verdier");
		}
		else {
			this.beløp = start;
			this.renter = rente;
		}
	}
	
	public double getBalance() {
		return beløp;
	}
	
	double getInterestRate() {
		return renter;
	}
	
	public void setInterestRate(double IR) {
		if(IR < 0) {
			throw new IllegalArgumentException("xd");
		}
		else {
			this.renter = IR;
		}
	}
	
	public void deposit(double d) {
		if(d<0) {
			throw new IllegalArgumentException(":D");
		}
		else {
			beløp += d;
		}
	}
	
	public void withdraw(double w) {
		if(w<0 || (beløp-w)<0) {
			throw new IllegalArgumentException(":(");
		}
		else {
			beløp -= w;
		}
	}
	
	public void addInterest() {
		double tempI = (this.renter/100)*beløp;
		beløp += tempI;		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
