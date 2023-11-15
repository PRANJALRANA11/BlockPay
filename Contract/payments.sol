// // SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


contract Main {
    // Payment[] public payments;

    // struct Payment {
    //     address user;
    //     uint256 amount;
    // } 

    event PaymentReceived(address indexed user,uint256 amount);
    event Withdrawal(address indexed owner, uint256 ownerAmount, address indexed creator, uint256 creatorAmount);
    event retrieved(address indexed buyer, uint amount);


    function recieve()public payable{
        //  payments.push(Payment(msg.sender , msg.value));
         emit PaymentReceived(msg.sender,msg.value);
    }

    function getbalance()public view returns(uint) {
        return address(this).balance;
    }

    function withdraw(address payable creator, uint amount) public {
        // uint checkpay=checkPay(buyer);
        require(amount!=0,"insufficient amount");
        // require(checkpay!=0);
        uint256 ownerAmount = (amount * 15) / 1000;
        uint256 creatorAmount = amount - ownerAmount; 
        payable(0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2).transfer(ownerAmount);
        payable(creator).transfer(creatorAmount);   
        
        emit Withdrawal(0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2, ownerAmount, creator, creatorAmount);
    }

    function retrieve(address payable  buyer,uint amount)public {
        payable(buyer).transfer(amount);
        emit retrieved(buyer,amount);
    }

    // function checkPay(address user)internal view returns(uint256) {
    //     for (uint256 i = 0; i < payments.length; i++) {
    //         if (payments[i].user == user) {
    //             uint amount = payments[i].amount;
    //             return amount;
    //         }
    //     }
    //         return 0; // User not found
    //     }
    }
// 4000000000000000000 with 18 zero
