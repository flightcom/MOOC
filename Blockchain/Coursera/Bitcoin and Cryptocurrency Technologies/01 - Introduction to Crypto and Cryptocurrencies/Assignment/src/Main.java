
public class Main {

	public static void main (String[] args) {
		System.out.println("Hello !");
		UTXOPool utxoPool = new UTXOPool();
		TxHandler txHandler = new TxHandler(utxoPool);
	}
}