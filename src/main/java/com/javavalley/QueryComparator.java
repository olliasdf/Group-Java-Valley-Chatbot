package com.javavalley;

import java.util.Comparator;

public class QueryComparator implements Comparator<String> {
	StringSimilarity a = new StringSimilarity();
	String query;
	public QueryComparator(String b) {
	query = b;	
		
	}
	
	@Override
	public int compare(String o1, String o2) {
		
		System.out.println("currently comparing...");
		// TODO Auto-generated method stub
		if  (a.similarity(o1, query) > a.similarity(o2, query))
			return 1;
		if  (a.similarity(o1, query) < a.similarity(o2, query))
			return -1;
		
		return 0;
	}

}
