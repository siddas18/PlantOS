const webcam = (webcamElement, canvasElement) => {

    const adjustVideoSize = (width, height) => {
        const aspectRatio = width / height;
        if (width >= height) {
            webcamElement.width = aspectRatio * webcamElement.height;
        } else {
            webcamElement.height = webcamElement.width / aspectRatio;
        }
    }

    const setup = async () => {
        return new Promise((resolve, reject) => {
            if (navigator.mediaDevices.getUserMedia !== undefined) {
                navigator.mediaDevices.getUserMedia({
                    audio: false, video: { facingMode: 'user' }
                })
                    .then((mediaStream) => {
                        if ("srcObject" in webcamElement) {
                            webcamElement.srcObject = mediaStream;
                        } else {
                            // For older browsers without the srcObject.
                            webcamElement.src = window.URL.createObjectURL(mediaStream);
                        }
                        webcamElement.addEventListener(
                            'loadeddata',
                            async () => {
                                adjustVideoSize(
                                    webcamElement.videoWidth,
                                    webcamElement.videoHeight
                                );
                                resolve();
                            },
                            false
                        );
                    });
            } else {
                reject();
            }
        });
    }

    const _drawImage = () => {
        const imageWidth = webcamElement.videoWidth;
        const imageHeight = webcamElement.videoHeight;

        const context = canvasElement.getContext('2d');
        canvasElement.width = imageWidth;
        canvasElement.height = imageHeight;

        context.drawImage(webcamElement, 0, 0, imageWidth, imageHeight);
        return { imageHeight, imageWidth };
    }

    const takeBlobPhoto = () => {
        const { imageWidth, imageHeight } = _drawImage();
        return new Promise((resolve, reject) => {
            canvasElement.toBlob((blob) => {
                resolve({ blob, imageHeight, imageWidth });
            });
        });
    }

    const takeBase64Photo = ({ type, quality } = { type: 'png', quality: 1 }) => {
        const { imageHeight, imageWidth } = _drawImage();
        const base64 = canvasElement.toDataURL('image/' + type, quality);
        return { base64, imageHeight, imageWidth };
    }
}

export default webcam;