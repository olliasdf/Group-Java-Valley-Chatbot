/*package com.javavalley;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Path;
import java.text.ParseException;

import javax.management.Query;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.custom.CustomAnalyzer;
import org.apache.lucene.document.FieldType;
import org.apache.lucene.document.StringField;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexOptions;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;

public class IndexTest {
	
	public static Query turnStringIntoQuery(String string) throws IOException, ParseException {
	    Analyzer ana = CustomAnalyzer.builder()  
	        .withTokenizer("standard")
	          .addTokenFilter("lowercase")
	          .build();
	    Query q = new QueryParser( "text", ana).parse(string);
	    return q;
	    
	    
	  }
	
	private static String readFile(String file) throws IOException {
	    BufferedReader reader = new BufferedReader(new FileReader (file));
	    String         line = null;
	    StringBuilder  stringBuilder = new StringBuilder();
	    String         ls = System.getProperty("line.separator");

	    try {
	        while((line = reader.readLine()) != null) {
	            stringBuilder.append(line);
	            stringBuilder.append(ls);
	        }

	        return stringBuilder.toString();
	    } finally {
	        reader.close();
	    }
	}
	//reference: https://stackoverflow.com/questions/326390/how-do-i-create-a-java-string-from-the-contents-of-a-file

	
	  
	  
    
	  public static Path addDocToIndex(Document doc) throws IOException {
	    Analyzer ana = CustomAnalyzer.builder()  
	        .withTokenizer("standard")
	          .addTokenFilter("lowercase")
	          .build();
	    
	    File a = new File("Index"); 
	    Path p = a.toPath();
	    Directory dir = FSDirectory.open(p);
	    
	    
	    
	  
	    IndexWriterConfig indexWriterConfig = new IndexWriterConfig(ana);
	    IndexWriter writer = new IndexWriter(dir, indexWriterConfig);
	    writer.addDocument(doc);
	    writer.close();
	    return p;
	    
	  }
	  
	  

	  public static void main(String[] args) throws IOException, ParseException {
		  File a = new File("Index"); 
		    Path p = a.toPath();
		    
		    
		  String Path = "PythonScript/TextFiles/cricket.txt";
		  String firstFile = readFile(Path);
	      System.out.println(firstFile);
	      
	      String Path1 = "PythonScript/TextFiles/cancer.txt";
	      String secondFile = readFile(Path1);

		  
	     
		  
		  
		  FieldType customField = new FieldType(); //TextField does not store TermVector, so we need a Custom Field
	    customField.setStoreTermVectors(true);
	    customField.setIndexOptions(IndexOptions.DOCS_AND_FREQS_AND_POSITIONS_AND_OFFSETS);
	    customField.stored();
	    customField.setStoreTermVectorOffsets(true);
	    customField.setStoreTermVectorPositions(true);
	    customField.storeTermVectorOffsets();
	    customField.storeTermVectorPositions();
	    
	    customField.tokenized();
	    
	    
	    
	    Field satz1 = new StringField("text", firstFile, Field.Store.YES);
	    
	    
	    
	    Document doc1 = new Document(); //add docs, each containing one of the sentences
	    doc1.add(satz1);
	    addDocToIndex(doc1);
	    
	    Field satz2 = new Field("text", secondFile, customField);
	    
	    
	    
	    Document doc2 = new Document(); //add docs, each containing one of the sentences
	    doc2.add(satz2);
	    addDocToIndex(doc2);
	    
	    
	    
	    IndexReader reader = DirectoryReader.open(FSDirectory.open(p));
	    IndexSearcher searcher = new IndexSearcher(reader);
	    
	    Query sunny = turnStringIntoQuery("cricket");
	    
	    TopDocs ab = searcher.search(sunny, 10);
	   
	    ScoreDoc[] hit1 = ab.scoreDocs; //they are not sorted by docId and Arrays.sort doesnt work on them
	   
	  
	    System.out.println("Number of docs that contain the term: " + hit1.length); //doc freq
	    for (int i=0; i<hit1.length;i++) {
	      
	    System.out.println("docID"  + ":" +hit1[i]); //docid from docs that contain the term
	    
	    int doci = hit1[1].doc;
	    Document te = searcher.doc(doci);
	    System.out.println(hit1[i].doc);
	    
	    System.out.println("te.toString()" + te.toString());
	    System.out.println(te.get("text"));
	    
	    		
	    
	    
	    
	    //addDocToIndex(doc1);
	    
	    
	    
	    
	    
	    
	    
	    

	    
	    
	    
	    
	    }
	  // TODO Auto-generated method stub

	  }
}
*/
