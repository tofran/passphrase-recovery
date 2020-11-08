import React from 'react';
import { render } from 'react-dom';
import { PassphraseRecovery } from './components/PassphraseRecovery';

const Application: React.FunctionComponent = () => (
  <>
    <PassphraseRecovery />
  </>
)

render(<Application />, document.getElementById('root'))
