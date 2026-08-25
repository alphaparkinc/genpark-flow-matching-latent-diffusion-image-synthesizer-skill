from client import FlowMatchingLatentDiffusionImageSynthesizerClient

def main():
    client = FlowMatchingLatentDiffusionImageSynthesizerClient()
    res = client.synthesize_flux_diffusion_frame('An architect holding a glowing blueprint with legible typography: GENPARK AI', 1920, 1080, 28)
    print('Generation: ' + res['generation_id'] + ' (' + res['dimensions'] + ')')
    print('Text Rendering Accuracy: ' + str(res['text_render_accuracy_score_pct']) + '% | Steps: ' + str(res['flow_matching_euler_steps']))
    print('Artifact URL: ' + res['output_tensor_artifact_url'])

if __name__ == '__main__':
    main()
