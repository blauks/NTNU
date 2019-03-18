package interfaces;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;


public class CardDeck implements Predicate<Card>{

	private List<Card> deck = new ArrayList<>();
	
	public CardDeck(int n){
		
		for(int x = 1;x<=n;x++) {
			deck.add(new Card('S',x));
		}
		
		for(int x = 1;x<=n;x++) {
			deck.add(new Card('H',x));
		}
		
		for(int x = 1;x<=n;x++) {
			deck.add(new Card('D',x));
		}
		
		for(int x = 1;x<=n;x++) {
			deck.add(new Card('C',x));
		}
	}
	
	public int getCardCount() {
		return deck.size();
	}
	
	public Card getCard(int n) {
		if(n >= deck.size()) {
			throw new IllegalArgumentException();
		}
		return deck.get(n);
	}
	
	public void shufflePerfectly() {
		
		List<Card> shuffledDeck = new ArrayList<>();
		List<Card> firstHalf = this.deck.subList(0, deck.size()/2);
		List<Card> secondHalf = this.deck.subList(deck.size()/2, deck.size());
		
		shuffledDeck.add(firstHalf.get(0));
		for(int i = 1; i < firstHalf.size();i++) {
			shuffledDeck.add(secondHalf.get(i-1));
			shuffledDeck.add(firstHalf.get(i));
		}
		shuffledDeck.add(secondHalf.get(secondHalf.size()-1));
		this.deck = shuffledDeck;
		
		
	}
	
	public boolean hasCard(Predicate<Card> predicate) {
		for(Card kort : deck) {
			if(predicate.test(kort)) {
				return true;
			}
		}
		
		return false;
	}
	
	public int getCardCount(Predicate<Card> predicate) {
		int summ = 0;
		
		for(Card c:deck) {
			if(predicate.test(c)) {
				summ++;
			}
		}
		
		return summ;
	}
	
	public List<Card> getCards(Predicate<Card> predicate){
		List<Card> temp = new ArrayList<Card>();
		
		for(Card c:deck) {
			if(predicate.test(c)) {
				temp.add(c);
			}
		}
		
		return temp;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CardDeck cd = new CardDeck(5);
		
		System.out.println(cd.deck);
		cd.shufflePerfectly();
		System.out.println(cd.deck);
		
		Card xD = new Card('S',1);
		
		System.out.println(cd.hasCard((x) -> cd.deck.contains(xD)));
	}

	@Override
	public boolean test(Card t) {
		// TODO Auto-generated method stub
		return false;
	}

}
