import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        List<char[]> labyrinthList = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader("maps/map01.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                line = line.strip();
                if (!line.isEmpty()) {
                    labyrinthList.add(line.toCharArray());
                }
            }
        }
        char[][] labyrinth = labyrinthList.toArray(new char[0][]);

        int[] start = null, end = null;
        for (int i = 0; i < labyrinth.length; i++) {
            for (int j = 0; j < labyrinth[i].length; j++) {
                if (labyrinth[i][j] == 'A') start = new int[]{i, j};
                if (labyrinth[i][j] == 'B') end = new int[]{i, j};
            }
        }

        if (start == null || end == null) {
            System.out.println("Start or end not found");
            return;
        }

        if (isSolvable(labyrinth, start, end)) {
            System.out.println("Solvable");
        } else {
            System.out.println("Not solvable");
        }
    }

    static boolean isSolvable(char[][] labyrinth, int[] start, int[] end) {
        int rows = labyrinth.length, cols = labyrinth[0].length;
        boolean[][] visited = new boolean[rows][cols];
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(start);
        visited[start[0]][start[1]] = true;

        int[][] dirs = {{-1,0},{1,0},{0,-1},{0,1}};
        while (!queue.isEmpty()) {
            int[] pos = queue.poll();
            if (Arrays.equals(pos, end)) return true;
            for (int[] d : dirs) {
                int nx = pos[0] + d[0], ny = pos[1] + d[1];
                if (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
                    if (!visited[nx][ny] && (labyrinth[nx][ny] == '0' || labyrinth[nx][ny] == 'B')) {
                        visited[nx][ny] = true;
                        queue.add(new int[]{nx, ny});
                    }
                }
            }
        }
        return false;
    }
}
