package interfaces.twitter;

import java.util.Comparator;

public class TweetsCountComparator implements Comparator<TwitterAccount>{

	@Override
	public int compare(TwitterAccount o1, TwitterAccount o2) {
		if(o1.getTweetCount() < o2.getTweetCount()) {
			return 1;
		}
		else if(o1.getTweetCount() > o2.getTweetCount()){
			return -1;
		}

		return 0;
	}
	

}
