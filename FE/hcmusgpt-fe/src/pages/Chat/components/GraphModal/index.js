import { Modal, Tabs } from 'antd';
import { useEffect, useState } from 'react';
import LineChart from '../../../../components/LineChart';
import VerticalChart from '../../../../components/VerticalChart';
import { ALIAS } from '../../../../constants/alias';
import { PROVIDER } from '../../../../constants/provider';
import { TYPE_ANSWER } from '../../../../constants/typeAnswer';

const GraphModal = ({ ...props }) => {
    const { showModal, setShowModal, graph, type, providerAvailable } = props;

    const [tags, setTags] = useState([]);

    useEffect(() => {
        const temp = [
            {
                key: 1,
                label: PROVIDER.FIREANT,
                children:
                    type === TYPE_ANSWER.VERTICAL ? (
                        <VerticalChart
                            years={graph?.years}
                            dataRaw={Object.entries(graph[PROVIDER.FIREANT] ? graph[PROVIDER.FIREANT] : []).map(
                                ([key, values]) => {
                                    return {
                                        name: key,
                                        data: values.dataRaw,
                                    };
                                },
                            )}
                            title={ALIAS[graph?.title]}
                        />
                    ) : (
                        <LineChart
                            years={graph?.years}
                            dataRaw={Object.entries(graph[PROVIDER.FIREANT] ? graph[PROVIDER.FIREANT] : []).map(
                                ([key, values]) => {
                                    return {
                                        name: key,
                                        data: values.dataRaw,
                                    };
                                },
                            )}
                            title={ALIAS[graph?.title]}
                        />
                    ),
            },
            {
                key: 2,
                label: PROVIDER.VIETSTOCK,
                children:
                    type === TYPE_ANSWER.VERTICAL ? (
                        <VerticalChart
                            years={graph?.years}
                            dataRaw={Object.entries(graph[PROVIDER.VIETSTOCK] ? graph[PROVIDER.VIETSTOCK] : []).map(
                                ([key, values]) => {
                                    return {
                                        name: key,
                                        data: values.dataRaw,
                                    };
                                },
                            )}
                            title={ALIAS[graph?.title]}
                        />
                    ) : (
                        <LineChart
                            years={graph?.years}
                            dataRaw={Object.entries(graph[PROVIDER.VIETSTOCK] ? graph[PROVIDER.VIETSTOCK] : []).map(
                                ([key, values]) => {
                                    return {
                                        name: key,
                                        data: values.dataRaw,
                                    };
                                },
                            )}
                            title={ALIAS[graph?.title]}
                        />
                    ),
            },
            {
                key: 3,
                label: PROVIDER.CAFEF,
                children:
                    type === TYPE_ANSWER.VERTICAL ? (
                        <VerticalChart
                            years={graph?.years}
                            dataRaw={Object.entries(graph[PROVIDER.CAFEF] ? graph[PROVIDER.CAFEF] : []).map(
                                ([key, values]) => {
                                    return {
                                        name: key,
                                        data: values.dataRaw,
                                    };
                                },
                            )}
                            title={ALIAS[graph?.title]}
                        />
                    ) : (
                        <LineChart
                            years={graph?.years}
                            dataRaw={Object.entries(graph[PROVIDER.CAFEF] ? graph[PROVIDER.CAFEF] : []).map(
                                ([key, values]) => {
                                    return {
                                        name: key,
                                        data: values.dataRaw,
                                    };
                                },
                            )}
                            title={ALIAS[graph?.title]}
                        />
                    ),
            },
        ];
        setTags(temp);
    }, [graph, type]);

    const handleClose = () => {
        setShowModal(false);
    };

    return (
        <>
            <Modal
                width="65%"
                title={`Bảng ${ALIAS[graph?.title]}`}
                open={showModal}
                onCancel={handleClose}
                footer={null}
            >
                <Tabs size="middle" items={tags.filter((item) => providerAvailable?.includes(item?.label))} />
            </Modal>
        </>
    );
};

export default GraphModal;
