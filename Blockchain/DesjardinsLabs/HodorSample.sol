pragma solidity ^0.4.18;

contract Escrow {
    address public buyer;
    address public seller;
    
    enum State { AWAITING_PAYMENT, AWAITING_DELIVERY, COMPLETE }
    
    State public currentState;
    
    function Escrow(address _buyer, address _seller) public {
        buyer = _buyer;
        seller = _seller;
    }
    
    function confirmPayment() public payable {
        require(msg.sender == buyer);
        require(currentState == State.AWAITING_PAYMENT);
        currentState = State.AWAITING_DELIVERY;
    }
    
    function confirmDelivery() public {
        require(msg.sender == buyer);
        require(currentState == State.AWAITING_DELIVERY);
        seller.transfer(this.balance);
        currentState = State.COMPLETE;
    }
}
