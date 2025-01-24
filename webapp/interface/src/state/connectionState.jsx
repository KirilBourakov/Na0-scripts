import { createContext, useContext, useState } from 'react';

const ConnectContext = createContext();

export const ConnectionProvider = ({ children }) => {
  const [state, setState] = useState({
    'connected': true
  });

  return (
    <ConnectContext.Provider value={{ state, setState }}>
      {children}
    </ConnectContext.Provider>
  );
};

export const useConnectContext = () => useContext(ConnectContext);