import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class TxHandler {

    private final UTXOPool utxoPool;

    /**
     * Creates a public ledger whose current UTXOPool (collection of unspent transaction outputs) is
     * {@code utxoPool}. This should make a copy of utxoPool by using the UTXOPool(UTXOPool uPool)
     * constructor.
     */
    public TxHandler(UTXOPool utxoPool) {
        // IMPLEMENT THIS
        this.utxoPool = utxoPool;
    }

    /**
     * @return true if:
     * (1) all outputs claimed by {@code tx} are in the current UTXO pool, 
     * (2) the signatures on each input of {@code tx} are valid, 
     * (3) no UTXO is claimed multiple times by {@code tx},
     * (4) all of {@code tx}s output values are non-negative, and
     * (5) the sum of {@code tx}s input values is greater than or equal to the sum of its output
     *     values; and false otherwise.
     */
    public boolean isValidTx(Transaction tx) {
        // IMPLEMENT THIS
        // (1) all outputs claimed by {@code tx} are in the current UTXO pool
        for (int i = 0; i < tx.numInputs(); i++) {
            Transaction.Input inT = tx.getInput(i);
            UTXO utxo = new UTXO(inT.prevTxHash, inT.outputIndex);
            if (!utxoPool.contains(utxo)) {
                return false;
            };
        }

        // (2) the signatures on each input of {@code tx} are valid
        for (int i = 0; i < tx.numInputs(); i++) {
            Transaction.Input inT = tx.getInput(i);
            UTXO utxo = new UTXO(inT.prevTxHash, inT.outputIndex);
            if (!Crypto.verifySignature(
                utxoPool.getTxOutput(utxo).address,
                tx.getRawDataToSign(i),
                inT.signature)) {
                return false;
            }
        }

        // (3) no UTXO is claimed multiple times by {@code tx}
        List<UTXO> listUTXOs = tx.getInputs()
            .stream()
            .map(input -> new UTXO(input.prevTxHash, input.outputIndex))
            .collect(Collectors.toList());
        if (!isAllUniqueTxs(tx, listUTXOs)) {
            return false;
        }

        // (4) all of {@code tx}s output values are non-negative
        for (int i = 0; i < tx.numOutputs(); i++) {
            Transaction.Output ouT = tx.getOutput(i);
            if (ouT.value < 0) return false;
        }

        // (5) the sum of {@code tx}s input values is greater than or equal to the sum of its 
        // output values; and false otherwise
        Double inputSum = listUTXOs
            .stream()
            .map(utxo -> utxoPool.getTxOutput(utxo).value)
            .collect(Collectors.summingDouble(f -> f));

        Double outputSum = tx.getOutputs()
            .stream()
            .map(output -> output.value)
            .collect(Collectors.summingDouble(f -> f));

        if (inputSum < outputSum) return false;

        return true;

    }

	private boolean isAllUniqueTxs(Transaction tx, List<UTXO> listUTXOs) {
		return tx.numInputs() == listUTXOs.stream().distinct().count();
	}

    /**
     * Handles each epoch by receiving an unordered array of proposed transactions, checking each
     * transaction for correctness, returning a mutually valid array of accepted transactions, and
     * updating the current UTXO pool as appropriate.
     */
    public Transaction[] handleTxs(Transaction[] possibleTxs) {
        // IMPLEMENT THIS
        List<Transaction> verifiedTxs =  Stream.of(possibleTxs)
            .filter(tx -> isValidTx(tx))
            .collect(Collectors.toList());

        for (int i = 0; i < verifiedTxs.size(); i++) {
            Transaction tx = verifiedTxs.get(i);
            for (int j = 0; j < tx.numInputs(); j++) {
                Transaction.Input input = tx.getInput(j);
                UTXO utxo = new UTXO(input.prevTxHash, input.outputIndex);
                utxoPool.removeUTXO(utxo);
            }
            for (int j = 0; j < tx.numOutputs(); j++) {
                Transaction.Output out = tx.getOutput(j);
                UTXO utxo = new UTXO(tx.getHash(), j);
                utxoPool.addUTXO(utxo, out);
            }
        }
        
        return verifiedTxs.toArray(new Transaction[verifiedTxs.size()]);
    }
}
