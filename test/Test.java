package test;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;


public class Test {
	
	public static void main(String[] args) throws Exception {
		
		URL url = new URL("https://www.naver.com/"); 
		
		HttpURLConnection con = (HttpURLConnection) url.openConnection();
		
		BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream()));
		
		String line = null;
		
		while((line = br.readLine()) != null) {
			System.out.println(line);
		}
		
		
		
		
		
		
	}

}
