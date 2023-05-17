/* eslint-disable jsx-a11y/alt-text */
import classNames from 'classnames/bind';
import { useEffect } from 'react';
import logo from '../../../../img/logo.png';
import { useAnswer } from '../../hooks';
import styles from './Answer.module.scss';
import { AnswerOption } from './AnswerOption';

const cx = classNames.bind(styles);
function Answer({ data }) {
    const answerHook = useAnswer(data);
    useEffect(() => {
        answerHook.processData();
    }, []);
    const { element, content, tables } = answerHook;
    return (
        <>
            {data && (
                <div className={cx('wrapper')}>
                    <div className={cx('icon-user')}>
                        <img className={cx('icon')} src={logo} />
                    </div>
                    <div className={cx('answer')}>
                        <p className={cx('content')}>{content}</p>
                        {element && (
                            <ul className={cx('list')}>
                                {element.map((item, index) => (
                                    <AnswerOption key={index} hook={answerHook} table={tables[item]} text={item} />
                                ))}
                            </ul>
                        )}
                    </div>
                </div>
            )}
        </>
    );
}

export default Answer;
