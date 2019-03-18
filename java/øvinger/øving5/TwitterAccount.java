package objectstructures;

import java.util.ArrayList;
import java.util.Arrays;

public class TwitterAccount {
		
	private String usrname;
	private ArrayList<String> following =  new ArrayList<String>();
	private ArrayList<Tweet> nmbrOT = new ArrayList<Tweet>();
	private ArrayList<String> rts = new ArrayList<String>();
	
	TwitterAccount(String name){
		this.usrname = name;
	}
	
	public String getUserName() {
		return usrname;
	}
	
	public void follow(TwitterAccount acc) {
		following.add(acc.getUserName());
	}
	
	public void unfollow(TwitterAccount acc) {
		following.remove(acc.getUserName());
	}
	
	public boolean isFollowing(TwitterAccount acc) {
		if(following.contains(acc.getUserName())) {
			return true;
		}
		return false;
	}
	
	public boolean isFollowedBy(TwitterAccount acc) {
		if(acc.isFollowing(this)) {
			return true;
		}
		return false;
	}
	
	public void tweet(String t) {
		Tweet nt = new Tweet(this,t);
		nmbrOT.add(0,nt);
	}
	
	public void retweet(Tweet ot) {
		Tweet rt = new Tweet(this,ot);
		if(!rts.contains(rt.toString())){
			rts.add(rt.toString());
			nmbrOT.add(0,rt);
		}
		else {
			ot.gotRTed(69);
		}
	}

	public Tweet getTweet(int i) {
		if(i<1) {
			throw new IllegalArgumentException();
		}
		return nmbrOT.get(i-1);
	}
	
	public int getTweetCount() {
		return nmbrOT.size();
	}
	
	public int getRetweetCount() {
		int summ = 0;
		
		for(Tweet y:nmbrOT) {
			summ += y.getRetweetCount();
			}
		return summ;

	}
	
	public static void main(String[] args) {
		
		TwitterAccount ole = new TwitterAccount("ole");
		TwitterAccount n = new TwitterAccount("nils");
		TwitterAccount k = new TwitterAccount("k");
		TwitterAccount p = new TwitterAccount("p");
		
		ole.tweet("Hei");
		p.tweet(" ");
		n.retweet(ole.getTweet(1));
		k.retweet(ole.getTweet(1));
		n.retweet(ole.getTweet(1));
		System.out.println(ole.getTweet(1));
		System.out.println(ole.getRetweetCount());
	}
	
}
