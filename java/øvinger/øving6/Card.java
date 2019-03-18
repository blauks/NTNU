package interfaces;

public class Card{

	
	private char color;
	private int nmbr;
	
	
	Card(char color, int nmbr){
		if(setColor(color) && setNumber(nmbr)) {
			this.color = color;
			this.nmbr = nmbr;
		}
		else {
			throw new IllegalArgumentException();
		}
		
	}
	
	private boolean setColor(char c) {
		if(!(c == 'S' || c == 'H' || c == 'D' || c == 'C')) {
			return false;
		}
		return true;
	}
	
	private boolean setNumber(int n) {
		if(n < 1 || n >13) {
			return false;
		}
		return true;
	}
	
	public char getSuit(){
		return this.color;
	}
	
	public int getFace() {
		return this.nmbr; 
	}
	
	public String toString() {
		return ""+color+nmbr;
	}
	
	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Card c = new Card('S',1);
		System.out.println(c.toString());
	}




}
