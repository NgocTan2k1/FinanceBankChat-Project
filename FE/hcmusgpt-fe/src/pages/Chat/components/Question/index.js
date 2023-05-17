/* eslint-disable jsx-a11y/alt-text */
import classNames from 'classnames/bind';

import { faUserSecret } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import styles from './Question.module.scss';
const cx = classNames.bind(styles);
function Question({ data }) {
    return (
        <>
            {data && (
                <div className={cx('wrapper')}>
                    <div className={cx('question')}>{`${data}`}</div>
                    <div className={cx('icon-user')}>
                        <FontAwesomeIcon className={cx('icon')} icon={faUserSecret} />
                    </div>
                </div>
            )}
        </>
    );
}

export default Question;
