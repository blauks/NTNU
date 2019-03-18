package interfaces.twitter;

import java.util.Comparator;


public class UserNameComparator implements Comparator<TwitterAccount>{
	
	@Override
	public int compare(TwitterAccount o1, TwitterAccount o2) {
		return o1.getUserName().compareTo(o2.getUserName());
	}
	

}
