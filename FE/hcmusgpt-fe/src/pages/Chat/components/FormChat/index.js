import classNames from 'classnames/bind';

import styles from './FormChat.module.scss';

const cx = classNames.bind(styles);

function FormChat({ children }) {
    return <div className={cx('wrapper')}>{children}</div>;
}

export default FormChat;
