/**
 * A simple thread pool API.
 * 
 * Tasks that wish to get run by the thread pool must implement the
 * java.lang.Runnable interface.
 */
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ThreadPool
{
	
	private ExecutorService pool;

	/**
	 * Create a default size thread pool.
 	 */
	public ThreadPool() {
		pool = Executors.newFixedThreadPool(10);
    }
	

	/**
	 * Create a thread pool with a specified size.
	 * 
	 * @param int size The number of threads in the pool.
	 */
	public ThreadPool(int size) {
		pool = Executors.newFixedThreadPool(size);
    }
	

	/**
	 * shut down the pool.
	 */
	public void shutdown() {
		pool.shutdown();
	}
	

	/**
	 * Add work to the queue.
	 */
	public void add(Runnable task) {
		pool.submit(task);
	}
}
