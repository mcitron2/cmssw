#ifndef RecoPixelVertexing_PixelTrackFitting_PixelTrackCleanerWrapper_H
#define RecoPixelVertexing_PixelTrackFitting_PixelTrackCleanerWrapper_H

#include "RecoPixelVertexing/PixelTrackFitting/interface/PixelTrackCleaner.h"
#include  "RecoPixelVertexing/PixelTrackFitting/interface/TracksWithHits.h"
#include <map>

class PixelTrackCleanerWrapper {
public: 
  PixelTrackCleanerWrapper(PixelTrackCleaner * tc) : theCleaner(tc) {}
  pixeltrackfitting::TracksWithTTRHs clean(
      const pixeltrackfitting::TracksWithTTRHs & initialT_TTRHs) {
    
    pixeltrackfitting::TracksWithRecHits initialT_TRHs;
    std::map<const TrackingRecHit *, TransientTrackingRecHit::ConstRecHitPointer> hitMap;

    for (pixeltrackfitting::TracksWithTTRHs::const_iterator it = initialT_TTRHs.begin(), iend = initialT_TTRHs.end(); it < iend; ++it) {
      SeedingHitSet ttrhs = it->second;
      std::vector<const TrackingRecHit *> trhs;
      for (unsigned int i=0, n=ttrhs.size(); i < n; ++i) { 
        const TrackingRecHit * trh = ttrhs[i]->hit();
        trhs.push_back(trh);
        hitMap[trh]=ttrhs[i];
      }
      initialT_TRHs.push_back( pixeltrackfitting::TrackWithRecHits(it->first, trhs) );
    }

    pixeltrackfitting::TracksWithRecHits finalT_TRHs = theCleaner->cleanTracks(initialT_TRHs);
    pixeltrackfitting::TracksWithTTRHs finalT_TTRHs;

    for (pixeltrackfitting::TracksWithRecHits::const_iterator it = finalT_TRHs.begin(), iend = finalT_TRHs.end(); it < iend; ++it) {
       const std::vector<const TrackingRecHit *> & trhs = it->second; 
       SeedingHitSet ttrhs;
       for (unsigned int i=0, n=trhs.size(); i < n; ++i) {
         const TrackingRecHit * trh = trhs[i];
         ttrhs.add( hitMap[trh]);
       }
       finalT_TTRHs.push_back( pixeltrackfitting::TrackWithTTRHs(it->first, ttrhs));
    }
    return finalT_TTRHs;
  }
private:
  PixelTrackCleaner * theCleaner;
};
#endif
