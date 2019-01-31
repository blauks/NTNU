package encapsulation;

import java.util.Date;


public class Person {

	private String navn;
	private String email;
	private Date bursdag;
	private char kjønn;
	
	private String[] landkoder = {"ad", "ae", "af", "ag", "ai", "al", "am", "ao", "aq", "ar", "as", "at", "au", "aw", "ax", "az", "ba", "bb", "bd", "be", "bf", "bg", "bh", "bi", "bj", "bl", "bm", "bn", "bo", "bq", "br", "bs", "bt", "bv", "bw", "by", "bz", "ca", "cc", "cd", "cf", "cg", "ch", "ci", "ck", "cl", "cm", "cn", "co", "cr", "cu", "cv", "cw", "cx", "cy", "cz", "de", "dj", "dk", "dm", "do", "dz", "ec", "ee", "eg", "eh", "er", "es", "et", "fi", "fj", "fk", "fm", "fo", "fr", "ga", "gb", "gd", "ge", "gf", "gg", "gh", "gi", "gl", "gm", "gn", "gp", "gq", "gr", "gs", "gt", "gu", "gw", "gy", "hk", "hm", "hn", "hr", "ht", "hu", "id", "ie", "il", "im", "in", "io", "iq", "ir", "is", "it", "je", "jm", "jo", "jp", "ke", "kg", "kh", "ki", "km", "kn", "kp", "kr", "kw", "ky", "kz", "la", "lb", "lc", "li", "lk", "lr", "ls", "lt", "lu", "lv", "ly", "ma", "mc", "md", "me", "mf", "mg", "mh", "mk", "ml", "mm", "mn", "mo", "mp", "mq", "mr", "ms", "mt", "mu", "mv", "mw", "mx", "my", "mz", "na", "nc", "ne", "nf", "ng", "ni", "nl", "no", "np", "nr", "nu", "nz", "om", "pa", "pe", "pf", "pg", "ph", "pk", "pl", "pm", "pn", "pr", "ps", "pt", "pw", "py", "qa", "re", "ro", "rs", "ru", "rw", "sa", "sb", "sc", "sd", "se", "sg", "sh", "si", "sj", "sk", "sl", "sm", "sn", "so", "sr", "ss", "st", "sv", "sx", "sy", "sz", "tc", "td", "tf", "tg", "th", "tj", "tk", "tl", "tm", "tn", "to", "tr", "tt", "tv", "tw", "tz", "ua", "ug", "um", "us", "uy", "uz", "va", "vc", "ve", "vg", "vi", "vn", "vu", "wf", "ws", "ye", "yt", "za", "zm", "zw"};
	
	public Person(){
		
	}
	
	public Person(String n, String e, Date b, char k) throws IllegalArgumentException {
		setName(n);
		setEmail(e);
		setBirthday(b);
		setGender(k);
	}
	
	public void setName(String n) {
		String[] splitta = n.split("\\s+");
		String navnT = n.replaceAll("\\s+","");
		if(splitta.length > 2 || splitta.length <=1) { throw new IllegalArgumentException(); }
		for(int x = 0; x < navnT.length(); x++) {
			if(!(Character.isLetter(navnT.charAt(x)))) {
				throw new IllegalArgumentException();
			}
		}
		if(navnT.length() <= 4) {
			throw new IllegalArgumentException();
		}
		this.navn = n;
	}
	
	public String getName() {
		return this.navn;
	}
	
	public void setEmail(String e) {
		if(e == null) {
			this.email = e;
		}
		
		System.out.println(e);
		
		String[] emailT = e.split("\\.");
		String[] etternavn = emailT[1].split("@");
		String emailN = emailT[0] + " " + etternavn[0];
		
		System.out.println(this.navn);
		System.out.println(emailN);
		
		if(emailN.toUpperCase().compareTo(this.navn.toUpperCase()) != 0) {
			throw new IllegalArgumentException();
		}
		
		if(emailT.length > 3 || emailT.length < 3) {
			throw new IllegalArgumentException();
		}
		
		if(!(emailT[1].contains("@"))){
			throw new IllegalArgumentException();
		}
		
		boolean lk = true;
		
		System.out.println(emailT[2]);
		
		for(int y = 0; y < landkoder.length; y++) {
			if(emailT[2].compareTo(landkoder[y])==0){
				lk = false;
				System.out.println("X");
			}
		}
		
		System.out.println(lk);
		
		if(lk) {
			System.out.println("test");
			throw new IllegalArgumentException();
		}
		
		this.email = e;
		
	}
	
	public String getEmail() {
		return this.email;
	}
	
	public void setBirthday(Date b) {
		Date iDag = new Date();
		
		System.out.println(iDag);
		System.out.println(b);
		
		if(iDag.before(b)) {
			throw new IllegalArgumentException();
		}
		else {
			this.bursdag = b;
		}
	}
	
	public Date getBirthday() {
		return this.bursdag;
	}
	
	public void setGender(char k) {
		if(!(k == 'M' || k == 'F' || k == '\0')) {
			throw new IllegalArgumentException();
		}
		this.kjønn = k;
	}
	
	public char getGender() {
		return this.kjønn;
	}
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Date bd = new Date(99,10,6);
		Person p = new Person("Ola Nordmann","Ola.Nordmann@gmail.no", bd, 'M');
	}

}
