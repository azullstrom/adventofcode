import java.util.Scanner;

public class DayOne {
	
	private static int[] swap(int[] arr, int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
		
		return arr;
	}
	
	private static void sortHighest(int[] arr) {
		for(int i = 0; i < arr.length; i++) {
			for(int j = i + 1; j < arr.length; j++) {
				if(arr[i] < arr[j]) {
					arr = swap(arr, i, j);
				}
			}
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] elf_inventory = new int[1000];
		
		for(int i = 0; i < elf_inventory.length; i++) {
			
			while(true) {
				String x = sc.nextLine();
				
				if(x.isEmpty()) {
					break;
				} else {
					elf_inventory[i] += Integer.parseInt(x);
				}
			}
			if(elf_inventory[i] == 0) {
				break;
			}
		}
		
		sortHighest(elf_inventory);
		
		System.out.println("Elf with most cals: " + elf_inventory[0]);
		
		int sum = 0;
		for(int i = 0; i < 3; i++) {
			sum += elf_inventory[i];
		}
		System.out.println("Three elves with most cals summed: " + sum);
	}
}

