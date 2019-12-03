from app import app, db, redis_store, utils
from app.models import Bank, Branch, BankAccount, Tin, CountryofResidence, CountryinAddress, PostalCode, Account, Form

import requests
import datetime
from flask import Flask, jsonify, g, render_template, redirect, request

@app.route('/branch', methods=['GET'])
def get_branches():
    branches = Branch.query.all()
    if len(branches) == 0:
        branchNames = [
            "BPI UP Town Center",
            "BPI Loyola-Katipunan",
            "BDO Katipunan",
            "Metrobank Katipunan",
            "Metrobank Blue Ridge"
        ]
        branchAddresses = [
            "Unit C145A L1 Phase 2, UP Town Center, Katipunan Avenue, Quezon City",
            "299 Katipunan Avenue, Quezon City",
            "Regis Center, 327 Katipunan Avenue, Quezon City",
            "339 Katipunan Avenue, Quezon City",
            "222 Katipunan Avenue, Quezon City"
        ]
        bankNames = [
            "Bank of the Philippine Islands",
            "Bank of the Philippine Islands",
            "Banco de Oro",
            "Metrobank",
            "Metrobank"
        ]
        for i in range(0,len(branchNames)):
            branch = Branch(
                bankBranchName=branchNames[i],
                bankBranchAddress=branchAddresses[i],
                bankName=bankNames[i]
            )
            db.session.add(branch)
        db.session.commit()
        return get_branches()
    else:
        return_data = []
        for branch in branches:
            bankaccounts = branch.bankAccounts
            bankaccount_list = []
            for bankaccount in bankaccounts:
                bankaccount_list.append(str(bankaccount.bankAcctNo))
            return_data.append({
                "bankBranchName": branch.bankBranchName,
                "bankBranchAddress": branch.bankBranchAddress,
                "bankName": branch.bankName,
                "bankAccounts": bankaccount_list
            })
        return jsonify(return_data)


@app.route('/branch/create', methods=['POST'])
def create_branch():
    post_data = request.get_json()
    bankBranchName = post_data.get('bankBranchName')
    bankBranchAddress = post_data.get('bankBranchAddress')
    bankName = post_data.get('bankName')
    bank = Bank.query.get(bankName)

    branch = Branch(
        bankBranchName=bankBranchName,
        bankBranchAddress=bankBranchAddress
    )

    db.session.add(branch)
    bank.bankBranches.append(branch)
    db.session.commit()

    return jsonify({'msg': "SUCCESS"})
