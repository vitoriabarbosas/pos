import React, { useEffect, useState } from "react";
import GlobalStyle from "./styles/global";
import Header from "./components/Header";
import Resume from "./components/Resume";
import Form from "./components/Form";

const App = () => {
  const data = localStorage.getItem("transactions");
  const [transactionsList, setTransactionsList] = useState(
    data ? JSON.parse(data) : []
  );
  const [income, setIncome] = useState(0);
  const [expense, setExpense] = useState(0);
  const [total, setTotal] = useState(0);

  useEffect(() => {
    const descExpense = transactionsList
      .filter((item) => item.expense)
      .map((transaction) => Number(transaction.desc));

    const descIncome = transactionsList
      .filter((item) => !item.expense)
      .map((transaction) => Number(transaction.desc));

    const amountIncome = transactionsList
      .filter((item) => !item.expense)
      .map((transaction) => Number(transaction.amount));

    const expense = descExpense.reduce((acc, cur) => acc + cur, 0).toFixed(0);
    const income = descIncome.reduce((acc, cur) => acc + cur, 0).toFixed(0);
    const totalincome = amountIncome.reduce((acc, cur) => acc + cur, 0).toFixed(0);

    const total = Math.abs(totalincome).toFixed(2);
    setIncome(`${income}`);
    setExpense(`${expense}`);
    setTotal(`R$ ${total}`);
  }, [transactionsList]);

  const handleAdd = (transaction) => {
    const newArrayTransactions = [...transactionsList, transaction];

    setTransactionsList(newArrayTransactions);

    localStorage.setItem("transactions", JSON.stringify(newArrayTransactions));
  };

  return (
    <>
      <Header />
      <Resume income={income} expense={expense} total={total} />
      <Form
        handleAdd={handleAdd}
        transactionsList={transactionsList}
        setTransactionsList={setTransactionsList}
      />
      <GlobalStyle />
    </>
  );
};

export default App;
