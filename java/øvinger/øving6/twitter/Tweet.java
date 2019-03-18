package interfaces.twitter;

public class Tweet {

	TwitterAccount acc;
	String tweet;
	int rtCounter = 0;
	int isRT = 0;
	Tweet original = null;
	
	
	Tweet(TwitterAccount a, String text){
		this.acc = a;
		this.tweet = text;
	}
	
	Tweet(TwitterAccount acc, Tweet t){
		if(acc == t.getOwner()) {
			throw new RuntimeException();
		}
		this.acc = acc;
		this.tweet = t.getText();
		this.isRT = 1;
		if(t.isRT == 0) {
			this.original = t;
		}
		else {
			this.original = t.getOriginalTweet();
		}
		
		t.gotRTed(0);
	}
	
	public void gotRTed(int x) {
		if(x == 0 && getOriginalTweet() == null) {
			this.rtCounter++;
		}
		else if(x == 0 && getOriginalTweet() != null){
			this.getOriginalTweet().gotRTed(0);
		}
		else {
			this.rtCounter--;
		}
		
		
	}
	
	
	public String getText() {
		return this.tweet;
	}
	
	public TwitterAccount getOwner() {
		return this.acc;
	}
	
	public Tweet getOriginalTweet() {
		if(isRT == 0) {
			return null;
		}
		else {
			return original;
		}
		
	}
	
	public String toString() {
		return(acc.getUserName()+" "+ this.getText());
	}
	
	public int getRetweetCount() {
		return rtCounter;
	}
	
}
