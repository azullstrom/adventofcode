import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

class RockPaperScissors {
	
	public RockPaperScissors() {
		// TODO Auto-generated constructor stub
	}
	
	public ArrayList<String> getEncryptedStrategyGuideFromFrienemy(String input) throws FileNotFoundException {
		
		Scanner sc = new Scanner(new File(input));
		ArrayList<String> frienemyGuide = new ArrayList<String>();
		
		while (sc.hasNext()){
		    frienemyGuide.add(sc.next());
		}
		sc.close();
		
		return frienemyGuide;
	}

	public int getPointsAfterComparingRounds(ArrayList<String> frienemyGuide) {
		int points = 0;
		
		for(int i = 0; i < frienemyGuide.size() - 1; i++) {
			if(i % 2 == 0) {
				String theirMove = getElfMove(frienemyGuide.get(i));
				String yourMove = getElfMove(frienemyGuide.get(i + 1));
				
				points += getElfPoints(theirMove, yourMove);
			}
		}
		
		return points;
	}
	
	// Part two
	public int getPointsAfterAdditionalInfo(ArrayList<String> frienemyGuide) {
		int points = 0;
		
		for(int i = 0; i < frienemyGuide.size() - 1; i++) {
			if(i % 2 == 0) {
				String theirMove = getElfMove(frienemyGuide.get(i));
				String yourMove = frienemyGuide.get(i + 1);
				
				points += getElfPointsAfterAdditionalInfo(theirMove, yourMove);
			}
		}
		
		return points;
	}
	
	// Part two
	private int getElfPointsAfterAdditionalInfo(String theirMove, String yourMove) {
		int points = 0, rock = 1, paper = 2, scissors = 3, win = 6, draw = 3;
		
		// You have to lose
		if(yourMove.contains("X")) {
			if(theirMove == "rock") {
				points = scissors;
			}
			else if(theirMove == "paper") {
				points = rock;
			}
			else {
				points = paper;
			}
		}
		// You have to draw
		else if(yourMove.contains("Y")) {
			if(theirMove == "rock") {
				points = rock + draw;
			}
			else if(theirMove == "paper") {
				points = paper + draw;
			}
			else {
				points = scissors + draw;
			}
		}
		// You have to win
		else {
			if(theirMove == "rock") {
				points = paper + win;;
			}
			else if(theirMove == "paper") {
				points = scissors + win;;
			}
			else {
				points = rock + win;
			}
		}
		
		return points;
	}

	private int getElfPoints(String theirMove, String yourMove) {
		int points = 0, rock = 1, paper = 2, scissors = 3, win = 6, draw = 3;
		
		// Draw
		if(theirMove == yourMove && theirMove == "rock") {
			points = rock + draw;
		}
		else if(theirMove == yourMove && theirMove == "paper") {
			points = paper + draw;
		}
		else if(theirMove == yourMove && theirMove == "scissors") {
			points = scissors + draw;
		}
		// You win
		else if(theirMove == "rock" && yourMove == "paper") {
			points = paper + win;
		}
		else if(theirMove == "paper" && yourMove == "scissors") {
			points = scissors + win;
		}
		else if(theirMove == "scissors" && yourMove == "rock") {
			points = rock + win;
		}
		// You lose
		else {
			if(yourMove == "rock") {
				points = rock;
			}
			else if(yourMove == "paper") {
				points = paper;
			} 
			else {
				points = scissors;
			}
		}
		
		return points;
	}

	private String getElfMove(String move) {
		String rock = "AX", paper = "BY", scissors = "CZ";
		String elfHandFormation = null;
		
		if(rock.contains(move)) {
			elfHandFormation = "rock";
		} 
		else if(paper.contains(move)) {
			elfHandFormation = "paper";
		} 
		else if(scissors.contains(move)){
			elfHandFormation = "scissors";
		}
		
		return elfHandFormation;
	}
}

public class DayTwo {

	public static void main(String[] args) throws FileNotFoundException {
		// Part 1
		RockPaperScissors elf = new RockPaperScissors();
		ArrayList<String> frienemyGuide = elf.getEncryptedStrategyGuideFromFrienemy("./src/input.txt");
		int points = elf.getPointsAfterComparingRounds(frienemyGuide);
		
		System.out.println("Points after elf tournament: " + points + "\n");
		
		// Part 2
		points = elf.getPointsAfterAdditionalInfo(frienemyGuide);
		
		System.out.println("Points after elf tournament\nwith additional info from the busy elf: " + points);
	}

}
