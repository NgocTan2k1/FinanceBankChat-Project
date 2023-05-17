import classNames from 'classnames/bind';
import { useState } from 'react';
import { ALIAS } from '../../../../constants/alias';
import GraphModal from '../GraphModal';
import styles from './Answer.module.scss';

const cx = classNames.bind(styles);
export const AnswerOption = ({ key, text, table, hook }) => {
    const { type } = hook;
    const [providerAvailable, setProviderAvailable] = useState([]);
    const [showModal, setShowModal] = useState(false);
    useState(() => {
        setProviderAvailable(Object.keys(table).filter((item) => !['title', 'years'].includes(item)));
    }, [table]);

    return (
        <>
            <li
                id={key}
                onClick={(e) => {
                    setShowModal(true);
                }}
                className={cx('answer-option')}
            >
                {ALIAS[text]}
            </li>
            <GraphModal
                graph={table}
                providerAvailable={providerAvailable}
                setProviderAvailable={setProviderAvailable}
                showModal={showModal}
                type={type}
                setShowModal={setShowModal}
            />
        </>
    );
};
